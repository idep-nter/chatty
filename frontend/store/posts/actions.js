import axios from 'axios';

export default {
  async loadPosts(context, data) {
    const response = await axios.get(`http://localhost:8000/api/posts`);
  
    const posts = [];
  
    for (const key in response.data) {
      const post = {
        id: String(response.data[key].id),
        author: response.data[key].author,
        thread: response.data[key].thread,
        content: response.data[key].content,
      };
      posts.push(post);
    }
    context.commit('setPosts', posts);
  },
}



