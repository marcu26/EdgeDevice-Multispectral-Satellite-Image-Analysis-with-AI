namespace MicroControllersAPI.Dto.AnalaizeResults
{
    public class GetAnalizeResultsDto
    {
        public long Id { get; set; }
        public string RgbImage { get; set; }
        public string Overlay { get; set; }
        public string Sentinel2Image { get; set; }
        public string Mask { get; set; }
        public decimal UnusablePercentage { get; set; }
        public decimal Longitude { get; set; }
        public decimal Latitude { get; set; }
        public string Location { get; set; }
        public string CreatedAt { get; set; }
    }
}

