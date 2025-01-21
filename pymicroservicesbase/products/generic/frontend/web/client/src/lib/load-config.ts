import apiClient from '@/api/client';

export async function getStaticProps() {
    // Instead of fetching your `/api` route you can call the same
    // function directly in `getStaticProps`
    const response = await apiClient.loadApplicationConfig();
    const appConfig = await response.json();
    return { props: { appConfig } }
  }
