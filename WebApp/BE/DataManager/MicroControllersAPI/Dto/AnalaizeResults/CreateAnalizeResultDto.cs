namespace MicroControllersAPI.Dto.AnalaizeResults
{
    public class CreateAnalizeResultDto
    {
        public string Base64ImageRGB { get; set; }
        public string Base64OverlayRGB { get; set; }
        public string Base64ImageSentinel2 { get; set; }
        public string Base64Mask { get; set; }
        public decimal UnusablePercentage { get; set; }
        public decimal Longitude { get; set; }
        public decimal Latitude { get; set; }
    }
}

