namespace MicroControllersAPI.Utils.Pageable
{
    public class PageablePostModel
    {
        public int draw { get; set; }
        public int start { get; set; }
        public int length { get; set; }
        public string? SortField { get; set; }
        public bool? IsDescending { get; set; }
    }
}
