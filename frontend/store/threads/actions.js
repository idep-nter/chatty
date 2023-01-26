import axios from 'axios';

export default {
  async addThread(context, data) {
    const tags = context.getters.getTags
    // const new_tags = []
    // for (const tag in data.tags) {
    //   if (!tag in tags) {
    //     new_tags.push(tag)
    //   }
    // }
    // const threadData = {
    //   title: data.name,
    //   description: data.description,
    //   tags: data.tags,
    // };

    // await axios({
    //   method: 'post',
    //   url: 'http://localhost:8000/api/threads/',
    //   data: threadData,
    // });

    // context.commit('addThread', threadData);
    // this.$router.replace('/threads');
  },
  async addTag(context, data) {
    const tagData = {
      name: data.name,
    };
    await axios({
      method: 'post',
      url: 'http://localhost:8000/api/tags/',
      data: tagData,
    });
    context.commit('addTag', tagData);
  },
  async loadThreads(context, data) {
    const response = await axios.get(
      `http://localhost:8000/api/threads`
    );

    const threads = [];

    for (const key in response.data) {
      const thread = {
        id: String(response.data[key].id),
        name: response.data[key].title,
        tags: response.data[key].tags,
        description: response.data[key].description,
      };
      threads.push(thread);
    }
    context.commit('setThreads', threads);
  },
  async loadTags(context, data) {
    const response = await axios.get(
      `http://localhost:8000/api/tags`
    );

    const tags = [];

    for (const key in response.data) {
      const tag = {
        id: String(response.data[key].id),
        name: response.data[key].name,
      };
      tags.push(tag);
    }

    context.commit('setTags', tags);
  },
  // async loadPosts(context, data) {
  //   const response = await axios.get(
  //     `http://localhost:8000/api/posts`
  //   );

  //   const posts = [];

  //   for (const key in response.data.results) {
  //     const post = {
  //       id: String(response.data.results[key].id),
  //       author: response.data.results[key].author,
  //       thread: response.data.results[key].thread,
  //       content: response.data.results[key].content,
  //     };
  //     posts.push(post);
  //   }

  //   context.commit('setPosts', posts);
  // },
};
