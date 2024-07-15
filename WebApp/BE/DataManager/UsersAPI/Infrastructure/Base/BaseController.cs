using Microsoft.AspNetCore.Mvc;

namespace MicroControllersAPI.Infrastructure.Base
{
    public class BaseController : ControllerBase
    {
        protected int GetUserId()
        {
            string strUserId = User.Claims.FirstOrDefault(claim => claim.Type == "UserId")?.Value;
            try
            {
                var userId = int.Parse(strUserId);
                return userId;
            }
            catch
            {
                throw new Exception("Invalid jwt");
            }
        }
    }
}
