using MicroControllersAPI.Database.Context;
using MicroControllersAPI.Database.Entities;
using MicroControllersAPI.Infrastructure.Base;

namespace MicroControllersAPI.Repos
{
    public class RolesRepo : BaseRepository<Role>
    {
        private DatabaseContext _dbContext { get; set; }
        public RolesRepo(DatabaseContext dbContext) : base(dbContext)
        {
            _dbContext = dbContext;
        }
    }
}
