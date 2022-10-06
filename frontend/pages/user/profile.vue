<template>
  <div>
    <v-row class="mt-12 d-flex justify-center">
      <v-container class="justify-center d-flex">
        <v-col md="1">
          <v-card
            class="portrait"
            :img="userInfo.image"
            height="150"
            width="150"
            v-bind="attrs"
            v-on="on"
          ></v-card>
        </v-col>
      </v-container>
      <v-container class="justify-center d-flex information">
        <v-col md="4">
          <v-card max-width="600" height="500">
              <v-row>
                <v-col class="left mt-10">
                  <ul>
                    <li>USERNAME:</li>
                    <li>NAME:</li>
                    <li>EMAIL:</li>
                    <li>NUMBER OF POSTS</li>
                    <li>REGISTERED</li>
                  </ul>
                </v-col>
                <v-col class="right mt-10">
                  <ul>
                    <li>{{ userInfo.username }}</li>
                    <li>{{ userInfo.name }}</li>
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
          </v-card>
        </v-col>
      </v-container>

      <v-container class="justify-center d-flex">
        <v-dialog v-model="editProfileDialog" max-width="600px">
          <template v-slot:activator="{ on, attrs }">
            <v-btn v-bind="attrs" v-on="on" color="primary">Edit profile</v-btn>
          </template>
          <edit-profile-dialog></edit-profile-dialog>
        </v-dialog>
      </v-container>
    </v-row>
  </div>
</template>

<script>
import EditProfileDialog from '~/components/dialogs/EditProfileDialog.vue';

export default {
  components: { EditProfileDialog },
  data() {
    return {
      editProfileDialog: false,
      userInfo: null,
      id: '1',
    };
  },
  methods: {},
  created() {
    this.userInfo = this.$store.getters['users/getUserInfo'](this.id);
  },
};
</script>

<style lang="scss" scoped>
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
