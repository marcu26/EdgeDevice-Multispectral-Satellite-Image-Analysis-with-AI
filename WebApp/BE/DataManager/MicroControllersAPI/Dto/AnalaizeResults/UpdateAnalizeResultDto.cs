namespace MicroControllersAPI.Dto.AnalaizeResults
{
    public class UpdateAnalizeResultDto
    {
        public int Id { get; set; }
        public decimal? UnusablePercentage { get; set; }
        public string? MicrocontrollerName { get; set; }
    }
}