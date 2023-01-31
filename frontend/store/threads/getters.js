import state from './state';

export default {
  getThreads(state) {
    return state.threads;
  },
  getTags(state) {
    return state.tags;
  },
  getThreadById: (state) => (payload) => {
    return state.threads.find((thread) => thread.id == payload);
  },
  hasPosts: (state) => (payload) => {
    const thread = this.getThreadById(payload);
    return thread.posts && thread.posts.length > 0;
  },
  getThreadTags: (state) => (payload) => {
    return state.tags.filter((tag) => payload.includes(tag.id));
  },
  getTagByName: (state) => (payload) => {
    return state.tags.find((tag) => tag.name == payload);
  },
  getThreadPosts: (state) => (payload) => {
    return state.posts.filter((post) => post.thread == payload);
  },
  getPosts(state) {
    return state.posts;
  },
};
