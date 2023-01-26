export default {
  addThread(state, payload) {
    state.threads.push(payload);
  },
  addTag(state, payload) {
    state.tags.push(payload);
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