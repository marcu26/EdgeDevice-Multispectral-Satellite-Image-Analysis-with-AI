namespace MicroControllersAPI.Utils.Pageable
{
    public class PageableDto<T>
    {
        public int TotalNumberOfRows { get; set; }
        public int NumberOfFilteredRows { get; set; }
        public List<T> Page { get; set; }  
    }
}
