using System.Security.Cryptography.X509Certificates;
using MicroControllersAPI.Dto.Roles;
using MicroControllersAPI.Repos;

namespace MicroControllersAPI.Services
{
    public class RolesService
    {
        public RolesRepo _rolesRepo { get; set; }
        public RolesService(RolesRepo rolesRepo) 
        {
            _rolesRepo = rolesRepo;
        }

        public async Task<List<GetRoleDto>> GetRolesAsync() 
        {
            var roles = await _rolesRepo.GetAllAsync();

            return roles.Select(role => new GetRoleDto
            {
                Id = role.Id,  
                Name = role.Name
            }).ToList();
        }
    }
}
