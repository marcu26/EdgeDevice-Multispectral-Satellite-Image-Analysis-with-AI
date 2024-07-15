using Microsoft.AspNetCore.SignalR;

namespace MicroControllersAPI.Services
{
    public class NotifyHub : Hub
    {
        public Task SendBroadcastMessage(string message)
        {
            return Clients.All.SendAsync("ReceiveMessage", "hello");
        }
    }
}
