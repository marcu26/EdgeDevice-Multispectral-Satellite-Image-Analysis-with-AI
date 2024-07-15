using Microsoft.IdentityModel.Tokens;
using System.IdentityModel.Tokens.Jwt;
using System.Security.Claims;
using System.Text;
using MicroControllersAPI.Database.Entities;
using MicroControllersAPI.Infrastructure.Config;
using Claim = System.Security.Claims.Claim;

namespace Core.Handlers
{
    public class AuthTokensHandler
    {
        public AuthTokensHandler()
        {

        }

        public string GenerateToken(User user)
        {

            var key = new SymmetricSecurityKey(Encoding.UTF8.GetBytes(AppConfig.JwtConfiguration.SecretKey));

            var credentials = new SigningCredentials(key, SecurityAlgorithms.HmacSha256);


            var idClaim = new Claim("UserId", user.Id.ToString());

            var Claims = new List<Claim>
            {
                idClaim,
                new Claim("roles", user.Role.Name)
            };

            var tokenDescriptor = new SecurityTokenDescriptor
            {
                Subject = new ClaimsIdentity(Claims),
                SigningCredentials = credentials,
                Audience = AppConfig.JwtConfiguration.Audience,
                Issuer = AppConfig.JwtConfiguration.Issuer,
                Expires = DateTime.UtcNow.AddMonths(AppConfig.JwtConfiguration.JwtLifetimeInMonths)
            };

            var token = new JwtSecurityTokenHandler().CreateToken(tokenDescriptor);
            var tokenString = new JwtSecurityTokenHandler().WriteToken(token);

            return tokenString;
        }
    }
}
