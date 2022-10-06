export default {
  getPosts: (state) => (payload) => {
    return state.posts.filter((post) => post.thread == payload);
  },
};
