export default {
  addThread(state, payload) {
    state.threads.push(payload);
  },
  addTag(state, payload) {
    state.tags.push(payload);
  },
  addPost(state, payload) {
    state.posts.push(payload);
  },
  setThreads(state, payload) {
    state.threads = payload;
  },
  setTags(state, payload) {
    state.tags = payload;
  },
  setPosts(state, payload) {
    state.posts = payload;
  },
};