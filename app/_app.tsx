import 'nextra-theme-blog/style.css'
import '../styles/main.css'
import { AppProps } from 'next/app';
import Head from 'next/head';


export default function withNextra({ Component, pageProps }: {Component:any,pageProps:any}) {
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
