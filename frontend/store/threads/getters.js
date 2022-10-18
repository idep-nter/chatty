import state from "./state";

export default {
  getThreads(state) {
    return state.threads;
  },
  getThreadById: (state) => (payload) => {
    return state.threads.find((thread) => thread.id == payload);
  },
  hasPosts: (state) => (payload) => {
    const thread = this.getThreadById(payload)
    return thread.posts && thread.posts.length > 0;
  },
  getTags: (state) => (payload) => {
    return state.tags.filter((tag) => payload.includes(tag.id));
  }, 
};