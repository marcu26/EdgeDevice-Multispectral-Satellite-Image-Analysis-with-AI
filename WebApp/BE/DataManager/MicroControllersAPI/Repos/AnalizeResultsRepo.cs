using MicroControllersAPI.Database.Context;
using MicroControllersAPI.Database.Entities;
using MicroControllersAPI.Dto.AnalaizeResults;
using MicroControllersAPI.Extensions;
using MicroControllersAPI.Infrastructure.Base;
using MicroControllersAPI.Utils.Pageable;
using Microsoft.EntityFrameworkCore;

namespace MicroControllersAPI.Repos
{
    public class AnalizeResultsRepo : BaseRepository<AnalizeResult>
    {
        public DatabaseContext _dbContext { get; set; }

        public AnalizeResultsRepo(DatabaseContext dbContext) : base(dbContext)
        {
            _dbContext = dbContext;
        }

        public async Task<PageableDto<AnalizeResult>> GetAnalizeResultsPaginaAsync(PageablePostModelAnalizeResults payload)
        {
            var dto = new PageableDto<AnalizeResult>();

            var query = _dbContext.AnalizeResults
                .Where(ar => !ar.IsDeleted)
                .AsQueryable();

            dto.TotalNumberOfRows = await query.CountAsync();

            if (!String.IsNullOrEmpty(payload.Location)) 
                query = query.Where(ar => ar.Location.Contains(payload.Location));

            if (payload.StartDate.HasValue)
                query = query.Where(ar => ar.CreatedAt >= payload.StartDate);
            
            if (payload.EndDate.HasValue)
                query = query.Where(ar => ar.CreatedAt <= payload.EndDate);

            dto.NumberOfFilteredRows = await query.CountAsync();

            if (!string.IsNullOrEmpty(payload.SortField))
                query = query.OrderByField(payload.SortField, payload.IsDescending ?? true);

            else
                query = query.OrderByField("CreatedAt", true);

            dto.Page = await query.Skip(payload.start)
                                  .Take(payload.length)
                                  .ToListAsync();

            return dto;
        }
    }
}
