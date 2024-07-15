using MicroControllersAPI.Database.Entities;
using MicroControllersAPI.Dto.AnalaizeResults;
using MicroControllersAPI.Infrastructure.Config;
using MicroControllersAPI.Repos;
using MicroControllersAPI.Utils;
using MicroControllersAPI.Utils.Pageable;
using Microsoft.AspNetCore.SignalR;
using Newtonsoft.Json.Linq;

namespace MicroControllersAPI.Services
{
    public class AnalizeResultsService
    {
        private readonly IWebHostEnvironment _webHostEnvironment;
        private AnalizeResultsRepo _analizeResultsRepo;
        public IHubContext<NotifyHub> _hubContext { get; set; }

        public AnalizeResultsService(IWebHostEnvironment webHostEnvironment, AnalizeResultsRepo analizeResultsRepo, IHubContext<NotifyHub> hubContext)
        {
            _webHostEnvironment = webHostEnvironment;
            _analizeResultsRepo = analizeResultsRepo;
            _hubContext = hubContext;
        }

        public async Task CreateAnalizeResult(CreateAnalizeResultDto payload)
        {
            var analizeResult = new AnalizeResult
            {
                UnusablePercentage = payload.UnusablePercentage,
                Longitude = payload.Longitude,
                Latitude = payload.Latitude
            };

            var imagePath = ImageSaver.SaveImage(payload.Base64ImageRGB,payload.Base64OverlayRGB, payload.Base64ImageSentinel2, payload.Base64Mask, _webHostEnvironment.WebRootPath);

            analizeResult.ImagePath = imagePath;

            var client = new HttpClient();
            var request = new HttpRequestMessage(HttpMethod.Get, $"https://api.geoapify.com/v1/geocode/reverse?lat={payload.Latitude}&lon={payload.Longitude}&apiKey=d8f45b5ae83f400694ac8642b3cf9abe");

            var response = await client.SendAsync(request);
            response.EnsureSuccessStatusCode();

            var jsonResponse = await response.Content.ReadAsStringAsync();
            var parsedResponse = JObject.Parse(jsonResponse);

            var locationName = parsedResponse["features"]?[0]?["properties"]?["formatted"]?.ToString();

            if (!string.IsNullOrEmpty(locationName))
            {
                analizeResult.Location = locationName;
            }

            _analizeResultsRepo.Add(analizeResult);

            await _hubContext.Clients.All.SendAsync("ReciveMessage", new SendAnalizeResultDto
            {
                UnusablePercentage = analizeResult.UnusablePercentage,
                Latitude = analizeResult.Latitude,
                Longitude = analizeResult.Longitude,
                ImagePath = AppConfig.ServerConfig.Host + analizeResult.ImagePath,
                Location = analizeResult.Location
            });

            await _analizeResultsRepo._dbContext.SaveChangesAsync();
        }

        public async Task<PageableResponse> GetAnalizeResults(PageablePostModelAnalizeResults payload)
        {
            var results = await _analizeResultsRepo.GetAnalizeResultsPaginaAsync(payload);

            return new PageableResponse()
            {
                draw = payload.draw,
                recordTotal = results.TotalNumberOfRows,
                recordFiltered = results.NumberOfFilteredRows,
                data = results.Page.Select(ar => new GetAnalizeResultsDto
                {
                    Id = ar.Id,
                    UnusablePercentage = ar.UnusablePercentage,
                    Latitude = ar.Latitude,
                    Longitude = ar.Longitude,
                    Location = ar.Location,
                    RgbImage = AppConfig.ServerConfig.Host + "AnalizeResultsImages/" + ar.ImagePath + "_RGB.png",
                    Mask = AppConfig.ServerConfig.Host + "AnalizeResultsImages/" + ar.ImagePath + "_Mask.tif",
                    Overlay = AppConfig.ServerConfig.Host + "AnalizeResultsImages/" + ar.ImagePath + "_Overlay.png",
                    Sentinel2Image = AppConfig.ServerConfig.Host + "AnalizeResultsImages/" + ar.ImagePath + "_Sentinel2.tif",
                    CreatedAt = ar.CreatedAt.ToString("yyyy-MM-dd")
                })
            };
        }

        public async Task DelteAnalizeResult(int analizeResultId)
        {
            var analizeResults = await _analizeResultsRepo.GetByIdAsync(analizeResultId);

            if (analizeResults == null)
                throw new Exception($"Analize result with id {analizeResultId} does not exist.");

            if (analizeResults.IsDeleted)
                throw new Exception($"Analize result with id {analizeResultId} is deleted.");

            analizeResults.IsDeleted = true;

            await _analizeResultsRepo._dbContext.SaveChangesAsync();
        }

        public async Task UpdateAnalizeResultAsync(UpdateAnalizeResultDto payload)
        {
            var analizeResults = await _analizeResultsRepo.GetByIdAsync(payload.Id);

            if (payload.UnusablePercentage.HasValue)
                analizeResults.UnusablePercentage = payload.UnusablePercentage.Value;

            await _analizeResultsRepo._dbContext.SaveChangesAsync();
        }
    }
}
