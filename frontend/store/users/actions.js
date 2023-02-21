import axios from 'axios';

export default {
  async loadUsers(context, data) {
    const response = await axios.get(`http://0.0.0.0:8000/api/users/`);

    const users = [];

    for (const key in response.data) {
      const user = {
        id: String(response.data[key].id),
        username: response.data[key].username,
        firstName: response.data[key].first_name,
        lastName: response.data[key].last_name,
        email: response.data[key].email,
        image: response.data[key].image,
        aboutme: response.data[key].about_me,
        postNum: response.data[key].number_of_posts,
        registered: response.data[key].date_joined,
        password: response.data[key].password,
        // isOnline: response.data[key].is_online,
      };
      users.push(user);
    }
    context.commit('setUsers', users);
  },
  async editUser(context, data) {
    const userData = {
      username: data.username,
      email: data.email,
      password: data.password,
      first_name: data.firstName,
      last_name: data.lastName,
      email: data.email,
      image: data.image,
      about_me: data.aboutme,
    };
    console.log(userData);
    await axios({
      method: 'put',
      url: 'http://0.0.0.0:8000/api/users/' + data.id + '/',
      data: userData,
    });
  },
  async loadUserId(context, data) {
    const response = await axios.get(`http://localhost:8000/api/user-id/`);
    context.commit('setUserId', String(response.data));
  },
  async checkPassword(context, data) {
    const pswData = {
      psw: data,
    };
    const response = await axios({
      method: 'post',
      url: 'http://localhost:8000/api/check-password/',
      data: pswData,
    });
    return response.data
  },
  async loadOnlineUsers(context, data) {
    const response = await axios.get(`http://localhost:8000/api/online-users/`);
    console.log(response.data)
    // context.commit('setOnlineUsers', String(response.data));
  },
  async addPostCount(context, data) {
    await axios({
      method: 'put',
      url: 'http://0.0.0.0:8000/api/users/' + data.id + '/',
      data: {
        username: data.username,
        password: data.password,
        email: data.email,
        number_of_posts: data.postNum + 1,
      },
    });
  },
};
