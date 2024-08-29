import 'nextra-theme-blog/style.css'
import '../styles/main.css'
/** @type {import('nextra').NextConfig} */

export default function Nextra({ Component, pageProps }): string {
  return (
    
    <>
      <Head>
        <link
          type="page"
          title="projects"
          href="/projects.mdx"
        />
        <link
          rel="alternate"
          type="application/rss+xml"
          title="RSS"
          href="/feed.xml"
        />
        <link
          rel="preload"
          href="/fonts/Inter-roman.latin.var.woff2"
          as="font"
          type="font/woff2"
          crossOrigin="anonymous"
        />
      </Head>
      <Component {...pageProps} />
    </>
  )
}
