using Core.Handlers;
using Core.Utils;
using System.Security.Cryptography.X509Certificates;
using MicroControllersAPI.Dto.Roles;
using MicroControllersAPI.Dto.Users;
using MicroControllersAPI.Repos;

namespace MicroControllersAPI.Services
{
    public class UsersService
    {
        private UsersRepo _usersRepo { get; set; }
        private AuthTokensHandler handler = new AuthTokensHandler();

        public UsersService(UsersRepo usersRepo)
        {
            _usersRepo = usersRepo;
        }

        public async Task<LogInResponseDto> LogInAsync(LogInDto payload)
        {
            var user = await _usersRepo.LogInAsync(payload.email, payload.password);

            if (user == null)
                throw new Exception("Credentials does not match any user");

            return new LogInResponseDto
            {
                Id = user.Id,
                Token = handler.GenerateToken(user),
                UserName = user.FirstName + " " + user.LastName
            };
        }

        public async Task<LogInResponseDto> CreateUser(CreateUserDto payload)
        {
            if (await _usersRepo.Exists(payload.Email))
                throw new Exception($"User with email {payload.Email} allready exists");

            var user = new Database.Entities.User { Email = payload.Email, Password = Hasher.Sha256Hash(payload.Password), RoleId = 2, FirstName = payload.FirstName, LastName = payload.LastName };

            _usersRepo.Add(user);

            await _usersRepo._dbContext.SaveChangesAsync();


            user = await _usersRepo.LogInAsync(payload.Email, payload.Password);

            return new LogInResponseDto
            {
                Id = user.Id,
                Token = handler.GenerateToken(user),
                UserName = user.FirstName + " " + user.LastName
            };
        }

        public async Task UpdateUserRole(UpdateUserRoleDto payload)
        {
            var user = await _usersRepo.GetByIdAsync(payload.UserId);

            if (user == null)
                throw new Exception($"User with Id {payload.UserId} allready exists");

            if (user.IsDeleted)
                throw new Exception($"User with Id {payload.UserId} is deleted.");

            user.RoleId = payload.RoleId;

            await _usersRepo._dbContext.SaveChangesAsync();
        }

        public async Task<List<GetUsersDto>> GetUsers(string? email)
        {
            var users = await _usersRepo.GetAllAsync();

            if (!String.IsNullOrEmpty(email))
                users = users.Where(u => u.Email.ToUpper().Contains(email.ToUpper()));

            return users.Where(u => !u.IsDeleted).Select(u => new GetUsersDto
            {
                Id = u.Id,
                Email = u.Email
            }).ToList();
        }

        public async Task DeleteUser(int userId)
        {
            var user = await _usersRepo.GetByIdAsync(userId);

            if (user == null)
                throw new Exception($"User with Id {userId} allready exists");

            if (user.IsDeleted)
                throw new Exception($"User with Id {userId} is deleted.");

            user.IsDeleted = true;

            await _usersRepo._dbContext.SaveChangesAsync();
        }
    }
}
