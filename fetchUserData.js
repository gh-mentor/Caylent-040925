// Simulate an API call to fetch user data
async function fetchUserData(userId) {
    const apiUrl = `https://jsonplaceholder.typicode.com/users/${userId}`;
    try {
        console.log(`Fetching data for user ID: ${userId}...`);
        const response = await fetch(apiUrl);

        // Check if the response is OK (status 200-299)
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }

        const userData = await response.json();
        console.log("User data fetched successfully:", userData);

        // Process the user data (e.g., extract specific fields)
        const processedData = processUserData(userData);
        console.log("Processed user data:", processedData);

        return processedData;
    } catch (error) {
        console.error("Error fetching user data:", error.message);
        throw error; // Re-throw the error for further handling
    }
}

// Helper function to process user data
function processUserData(userData) {
    return {
        id: userData.id,
        name: userData.name,
        email: userData.email,
        company: userData.company.name,
        city: userData.address.city,
    };
}

// Main function to demonstrate the workflow
async function main() {
    try {
        const userId = 1; // Example user ID
        const user = await fetchUserData(userId);

        // Simulate another asynchronous operation (e.g., saving data)
        await saveUserData(user);
        console.log("User data saved successfully!");
    } catch (error) {
        console.error("An error occurred in the main workflow:", error.message);
    }
}

// Simulate saving user data asynchronously
async function saveUserData(user) {
    console.log("Saving user data...");
    return new Promise((resolve) => {
        setTimeout(() => {
            console.log("User data saved:", user);
            resolve();
        }, 2000); // Simulate a 2-second delay
    });
}

// Run the main function
main();