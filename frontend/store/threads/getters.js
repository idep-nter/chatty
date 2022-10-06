export default {
  getThreads(state) {
    return state.threads;
  },
  getThreadById: (state) => (payload) => {
    return state.threads.find((thread) => thread.id == payload);
  },
};