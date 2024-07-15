using System.Drawing;


namespace MicroControllersAPI.Utils
{
    public static class ImageSaver
    {
        public static string SaveImage(string base64ImageRGB, string base64OverlayRGB, string base64ImageSentinel2, string base64Mask, string path)
        {
            var fileName = $"AnalizeResults_{DateTime.UtcNow:yyyyMMddHHmmss}";

            var bytesRGB = Convert.FromBase64String(base64ImageRGB);
            var tiffFilePathRGB = Path.Combine(path, "AnalizeResultsImages", $"{fileName}_RGB.png");
            File.WriteAllBytes(tiffFilePathRGB, bytesRGB);

            var bytesOverlayRGB = Convert.FromBase64String(base64OverlayRGB);
            var tiffFilePathOverlayRGB = Path.Combine(path, "AnalizeResultsImages", $"{fileName}_Overlay.png");
            File.WriteAllBytes(tiffFilePathOverlayRGB, bytesOverlayRGB);

            var bytesSentinel2 = Convert.FromBase64String(base64ImageSentinel2);
            var tiffFilePathSentinel2 = Path.Combine(path, "AnalizeResultsImages", $"{fileName}_Sentinel2.tif");
            File.WriteAllBytes(tiffFilePathSentinel2, bytesSentinel2);

            var bytesMask = Convert.FromBase64String(base64Mask);
            var tiffFilePathMask = Path.Combine(path, "AnalizeResultsImages", $"{fileName}_Mask.tif");
            File.WriteAllBytes(tiffFilePathMask, bytesMask);

            return fileName;
        }
    }
}
