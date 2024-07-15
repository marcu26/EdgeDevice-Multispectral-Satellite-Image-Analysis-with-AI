using Core.Utils;
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Mvc;
using MicroControllersAPI.Dto.Roles;
using MicroControllersAPI.Dto.Users;
using MicroControllersAPI.Infrastructure.Base;
using MicroControllersAPI.Services;

namespace MicroControllersAPI.Controller
{
    [ApiController]
    [Route("/api/users")]
    [Authorize]
    public class UsersController : BaseController
    {
        private UsersService _usersService { get; set; }

        public UsersController(UsersService usersService)
        {
            _usersService = usersService;
        }

        [AllowAnonymous]
        [HttpPost("log-in")]
        public async Task<IActionResult> LogIn(LogInDto payload)
        {
            try
            {
                return Ok(await _usersService.LogInAsync(payload));
            }
            catch (Exception ex)
            {
                return BadRequest(new ExceptionModel() { ErrorType = "BACKEND ERROR", ExceptionMessage = ex.Message});
            }
        }

        [AllowAnonymous]
        [HttpPost("create")]
        public async Task<IActionResult> Create(CreateUserDto payload)
        {
            try
            {
                return Ok(await _usersService.CreateUser(payload));
            }
            catch (Exception ex)
            {
                return BadRequest(new ExceptionModel() { ErrorType = "BACKEND ERROR", ExceptionMessage = ex.Message });
            }
        }

        [HttpPut("update-role")]
        [Authorize(Roles = "Admin")]
        public async Task<IActionResult> UpdateUserRoleAsync(UpdateUserRoleDto payload)
        {
            try
            {
                await _usersService.UpdateUserRole(payload);
                return Ok();
            }
            catch (Exception ex)
            {
                return BadRequest(new ExceptionModel() { ErrorType = "BACKEND ERROR", ExceptionMessage = ex.Message });
            }
        }

        [HttpPost("get-users")]
        [Authorize(Roles = "Admin")]
        public async Task<IActionResult> GetUsers([FromBody] GetUsersRequestDto payload)
        {
            try
            {
                return Ok(await _usersService.GetUsers(payload.Email));
            }
            catch (Exception ex)
            {
                return BadRequest(new ExceptionModel() { ErrorType = "BACKEND ERROR", ExceptionMessage = ex.Message });
            }
        }

         [HttpPut("delete-user/{userId}")]
        [Authorize(Roles = "Admin")]
        public async Task<IActionResult> Delte([FromRoute] int userId)
        {
            try
            {
                await _usersService.DeleteUser(userId);
                return Ok();
            }
            catch (Exception ex)
            {
                return BadRequest(new ExceptionModel() { ErrorType = "BACKEND ERROR", ExceptionMessage = ex.Message });
            }
        }
    }
}
