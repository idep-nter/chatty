export default {
  getRooms(state) {
    return state.rooms;
  },
  getRoomById: (state) => (payload) => {
    return state.rooms.find((room) => room.id == payload);
  },
};