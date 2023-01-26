<template>
  <v-container class="justify-center d-flex information">
    <v-card min-width="600" height="819" class="mt-12">
      <v-row class="d-flex justify-center mt-10">
        <v-card
          class="portrait"
          :img="userInfo.image"
          height="150"
          width="150"
        ></v-card>
      </v-row>
      <v-row>
        <v-col class="left mt-10">
          <ul>
            <li>USERNAME:</li>
            <li>FIRST_NAME:</li>
            <li>LAST_NAME:</li>
            <li>EMAIL:</li>
            <li>NUMBER OF POSTS</li>
            <li>REGISTERED</li>
          </ul>
        </v-col>
        <v-col class="right mt-10">
          <ul>
            <li>{{ userInfo.username }}</li>
            <li>{{ userInfo.firstName }}</li>
            <li>{{ userInfo.lastName }}</li>
            <li>{{ userInfo.email }}</li>
            <li>{{ userInfo.postNum }}</li>
            <li>{{ userInfo.registered }}</li>
          </ul>
        </v-col>
      </v-row>
      <v-row class="about left mt-5">
        <li>ABOUT ME:</li>
      </v-row>
      <v-row class="about">
        <li>{{ userInfo.aboutme }}</li>
      </v-row>
      <!-- IF current user === this user -->
      <v-row class="justify-center d-flex editBtn">
        <v-dialog persistent v-model="editProfileDialog" max-width="600px">
          <template v-slot:activator="{ on, attrs }">
            <v-btn v-bind="attrs" v-on="on" color="primary">Edit profile</v-btn>
          </template>
          <edit-profile-dialog
            :user-info="userInfo"
            @save-data="saveData"
            @close-dialog="editProfileDialog = false"
          ></edit-profile-dialog>
        </v-dialog>
      </v-row>
    </v-card>
  </v-container>
</template>

<script>
import EditProfileDialog from '~/components/dialogs/EditProfileDialog.vue';

export default {
  components: { EditProfileDialog },
  data() {
    return {
      editProfileDialog: false,
      userInfo: '',
    };
  },
  methods: {
    saveData(payload) {},
  },
  created() {
    const id = this.$route.params.id;
    this.$store.dispatch('users/loadUsers');
    this.userInfo = this.$store.getters['users/getUserInfo'](id)
  },
};
</script>

<style lang="scss" scoped>
.editBtn {
  position: absolute;
  bottom: 5%;
  left: 0%;
  right: 0%;
}

li {
  list-style-type: none;
  margin-bottom: 10px;
}

.left {
  display: flex;
  justify-content: center;
  font-weight: bold;
  color: $primaryColor;
  // margin-right: 10px
}

.right {
  display: flex;
  justify-content: left;
  margin-right: 30px;
}

.about {
  display: flex;
  justify-content: center;
}

.information {
  font-size: 20px;
}
</style>
