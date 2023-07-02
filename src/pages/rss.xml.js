import rss from '@astrojs/rss';
import { getCollection } from 'astro:content';

export async function get(context) {
  const blog = await getCollection('blog');
  return rss({
    title: '~rosset-nocpes Blog',
    description: 'Feed for socials',
    site: context.site,
    items: blog.map((post) => ({
      title: post.data.title,
      pubDate: post.data.pubDate,
      customData: post.data.customData,
      link: `/blog/${post.slug}/`,
    })),
  });
}