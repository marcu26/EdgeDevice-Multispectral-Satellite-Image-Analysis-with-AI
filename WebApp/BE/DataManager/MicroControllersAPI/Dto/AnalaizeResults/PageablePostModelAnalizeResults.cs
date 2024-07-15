using MicroControllersAPI.Utils.Pageable;

namespace MicroControllersAPI.Dto.AnalaizeResults
{
    public class PageablePostModelAnalizeResults : PageablePostModel
    {
        public string? Location { get; set; }
        public DateTime? StartDate { get; set; }
        public DateTime? EndDate { get; set; }

    }
}