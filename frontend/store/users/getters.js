export default {
  getUserInfo: (state) => (payload) => {
    return state.users.find((user) => user.id == payload);
  },
};
