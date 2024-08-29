import React from "react"

const YEAR = new Date().getFullYear()

export default {
  padding: 3,
  footer: <p>MIT 2024 © sayasumajo.</p>,
  head: ({ title, meta }) => (
    <>
      {meta.description && (
        <meta name="description" content={meta.description} />
      )}
      {meta.tag && <meta name="keywords" content={meta.tag} />}
      {meta.author && <meta name="author" content={meta.author} />}
    </>
  ),
  readMore: 'Read More →',
  postFooter: null,
  darkMode: true,
/*
  navs: [
    {
      url: 'https://github.com/shuding/nextra',
      name: 'Nextra'
    }
  ]*/
}