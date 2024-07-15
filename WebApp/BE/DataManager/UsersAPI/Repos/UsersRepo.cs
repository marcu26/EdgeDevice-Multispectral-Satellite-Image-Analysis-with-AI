using Core.Utils;
using Microsoft.EntityFrameworkCore;
using MicroControllersAPI.Database.Context;
using MicroControllersAPI.Database.Entities;
using MicroControllersAPI.Dto.Users;
using MicroControllersAPI.Infrastructure.Base;

namespace MicroControllersAPI.Repos
{
    public class UsersRepo : BaseRepository<User>
    {
        public DatabaseContext _dbContext;
        public UsersRepo(DatabaseContext dbContex) : base(dbContex) 
        {
                _dbContext = dbContex;
        }

        public async Task<User> LogInAsync(string email, string password) 
        {
            return await _dbContext.Users
                .Include(u => u.Role)
                .FirstOrDefaultAsync(u => u.Email == email && u.Password == Hasher.Sha256Hash(password));
        }

        public async Task<bool> Exists (string email) 
        {
            return await _dbContext.Users.AnyAsync(u => u.Email == email);
        }
    }
}
