using Core.Utils;
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Mvc;
using MicroControllersAPI.Services;

namespace MicroControllersAPI.Controller
{
    [ApiController]
    [Route("/api/roles/")]
    [Authorize]
    public class RolesController : ControllerBase
    {
        public RolesService _rolesService { get; set; }

        public RolesController(RolesService rolesService)
        {
                _rolesService = rolesService;
        }

        [HttpGet("get-all")]
        [Authorize(Roles = "Admin")]
        public async Task<IActionResult> GetRoles()
        {
            try
            {
                return Ok(await _rolesService.GetRolesAsync());
            }
            catch (Exception ex)
            {
                return BadRequest(new ExceptionModel() { ErrorType = "BACKEND ERROR", ExceptionMessage = ex.Message });
            }
        }
    }
}
