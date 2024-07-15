namespace Infrastructure.Utils
{
    public static class JwtTokenUtils
    {
        public static string GetJwtToken(string rawToken)
        {
            if (string.IsNullOrEmpty(rawToken))
                throw new Exception("Bearer token is missing");

            if (!rawToken.StartsWith("Bearer"))
                throw new Exception("Bearer token is invalid or missing");

            var token = rawToken.Substring("Bearer ".Length).Trim();

            if (string.IsNullOrEmpty(token))
                throw new Exception("Bearer token is missing");

            return token;
        }
    }
}
