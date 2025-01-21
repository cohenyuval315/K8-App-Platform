import NProgress from 'nprogress';

// Utility to wrap operations with progress
export const withProgress = async (operation: () => Promise<any>) => {
  try {
    NProgress.start(); // Start progress bar
    const result = await operation(); // Perform the async operation
    return result; // Return the result of the operation
  } catch (error) {
    console.error(error); // Handle errors if needed
    throw error; // Re-throw to maintain error flow
  } finally {
    NProgress.done(); // End progress bar
  }
};
