using Core.Utils;
using MicroControllersAPI.Dto.AnalaizeResults;
using MicroControllersAPI.Infrastructure.Base;
using MicroControllersAPI.Services;
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Mvc;
using System.Net.Http.Headers;

namespace MicroControllersAPI.Controller
{
    [ApiController]
    [Route("/api/analize-results/")]
    public class AnalizeResultsController : BaseController
    {
        private AnalizeResultsService _analizeResultsService { get; set; }

        public AnalizeResultsController(AnalizeResultsService analizeResultsService)
        {
            _analizeResultsService = analizeResultsService;
        }

        [AllowAnonymous]
        [HttpPost("create")]
        public async Task<IActionResult> CreateAnalizeResults(CreateAnalizeResultDto payload)
        {
            try
            {
                await _analizeResultsService.CreateAnalizeResult(payload);
                return Ok();
            }
            catch (Exception ex)
            {
                return BadRequest(new ExceptionModel() { ErrorType = "BACKEND ERROR", ExceptionMessage = ex.Message });
            }
        }

        [Authorize]
        [HttpPost("get-analize-results-pageable")]
        public async Task<IActionResult> GetAnalizeResultsAsync([FromBody] PageablePostModelAnalizeResults payload)
        {
            try
            { 
                return Ok(await _analizeResultsService.GetAnalizeResults(payload));
            }
            catch (Exception ex)
            {
                return BadRequest(new ExceptionModel() { ErrorType = "BACKEND ERROR", ExceptionMessage = ex.Message });
            }
        }

        [Authorize(Roles = "Admin")]
        [HttpPut("delete/{analizeResultId}")]
        public async Task<IActionResult> DeleteAnalizeResult([FromRoute]int analizeResultId)
        {
            try
            {
                await _analizeResultsService.DelteAnalizeResult(analizeResultId);
                return Ok();
            }
            catch (Exception ex)
            {
                return BadRequest(new ExceptionModel() { ErrorType = "BACKEND ERROR", ExceptionMessage = ex.Message });
            }
        }

        [Authorize(Roles = "Admin, Editor")]
        [HttpPut("update")]
        public async Task<IActionResult> UpdateAnalizeResult([FromBody] UpdateAnalizeResultDto payload)
        {
            try
            {
                await _analizeResultsService.UpdateAnalizeResultAsync(payload);
                return Ok();
            }
            catch (Exception ex)
            {
                return BadRequest(new ExceptionModel() { ErrorType = "BACKEND ERROR", ExceptionMessage = ex.Message });
            }
        }

        [HttpGet("download-image-png/{imageName}")]
        [Authorize]
        public IActionResult DownloadImageRGB([FromRoute]string imageName)
        {
            try
            {
                var imagePath = Path.Combine(Directory.GetCurrentDirectory(), "wwwroot\\AnalizeResultsImages", imageName);

                var contentDisposition = new ContentDispositionHeaderValue("attachment")
                {
                    FileName = imageName
                };
                Response.Headers.Add("Content-Disposition", contentDisposition.ToString());

                return File(System.IO.File.OpenRead(imagePath), "image/png");
            }
            catch (Exception ex)
            {
                return BadRequest(new ExceptionModel() { ErrorType = "BACKEND ERROR", ExceptionMessage = ex.Message });
            }
        }
    }
}
