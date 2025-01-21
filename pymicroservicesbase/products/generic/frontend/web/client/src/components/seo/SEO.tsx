import { NextSeo } from 'next-seo'

export default function SEO(){

    const title = "";
    const titleTemplate = "";
    const description = "";
    return (
        <NextSeo
            noindex
            title={title}
            description={description}
            titleTemplate={titleTemplate}
            openGraph={{
            type: 'website',
            title,
            description,
            }}
        />

    )
}
