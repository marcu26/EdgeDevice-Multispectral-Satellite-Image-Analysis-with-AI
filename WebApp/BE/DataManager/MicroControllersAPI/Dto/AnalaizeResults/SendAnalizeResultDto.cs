namespace MicroControllersAPI.Dto.AnalaizeResults
{
    public class SendAnalizeResultDto
    {
        public string ImagePath { get; set; }
        public decimal UnusablePercentage { get; set; }
        public decimal Longitude { get; set; }
        public decimal Latitude { get; set; }
        public string Location { get; set; }
        public string MicrocontrollerName { get; set; }
    }
}

