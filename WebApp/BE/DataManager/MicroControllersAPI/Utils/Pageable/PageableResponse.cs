namespace MicroControllersAPI.Utils.Pageable
{
    public class PageableResponse
    {
        public int draw { get; set; }
        public int recordTotal { get; set; }
        public int recordFiltered { get; set; }
        public object data { get; set; }
    }
}
