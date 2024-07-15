# Project Setup Instructions

## Backend Overview
The backend of this project consists of two microservices developed using .NET 6. These microservices are:
1. **UserAPI**: This service handles all operations related to user management.
2. **DataAPI**: This service manages satellite images and inference results.

## Setting Up the Project

In order to start the project, you need to set both microservices as startup projects. Follow these steps:

1. **Open the Solution in Visual Studio**:
   - Open your solution file (.sln) in Visual Studio.

2. **Set Multiple Startup Projects**:
   - Right-click on the solution in the Solution Explorer.
   - Select **Properties**.
   - In the **Common Properties** section, select **Startup Project**.
   - Choose the option **Multiple startup projects**.
   - Set the action for both microservices to **Start**.

3. **Save and Run**:
   - Click **OK** to save the settings.
   - Run the solution to start both microservices.

By setting both microservices as startup projects, you ensure that the entire backend environment is initialized and ready for development or testing.

## Arhitecture

![Arhitecture](/images/ControllerServiceRepo.png)