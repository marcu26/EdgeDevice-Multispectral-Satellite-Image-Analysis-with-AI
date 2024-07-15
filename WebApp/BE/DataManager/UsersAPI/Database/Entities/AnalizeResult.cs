using MicroControllersAPI.Infrastructure.Base;

namespace MicroControllersAPI.Database.Entities
{
    public class AnalizeResult : BaseEntity
    {
        public string ImagePath { get; set; }
        public decimal UnusablePercentage { get; set; }
        public decimal Longitude { get; set; }
        public decimal Latitude { get; set; }
        public string Location { get; set; }
    }
}
