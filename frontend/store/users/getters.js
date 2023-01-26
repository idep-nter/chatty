export default {
  getUserInfo: (state) => (payload) => {
    return state.users.find((user) => user.id == payload);
  },
  getUserId(state) {
    return state.userId;
  },
  getUsers(state) {
    return state.users
  }
};
