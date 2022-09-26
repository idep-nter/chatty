<template>
  <v-card height="30px">
    <v-toolbar extend>
      <NuxtLink to="/" class="links">
        <v-row class="mr-1">
          <v-icon class="ml-5 mr-2 icon" medium> mdi-bird </v-icon>
          <v-toolbar-title class="headline font-weight-bold">{{
            title
          }}</v-toolbar-title>
        </v-row>
      </NuxtLink>
      <v-breadcrumbs :items="breadcrumbs">
        <template v-slot:item="{ item }">
          <v-breadcrumbs-item :href="item.href" :disabled="item.disabled">
            {{ item.text.toUpperCase() }}
          </v-breadcrumbs-item>
        </template>
      </v-breadcrumbs>
      <v-spacer></v-spacer>

      <div class="right">
        <template v-if="loggedIn">
          <div class="text-center">
            <v-menu offset-y>
              <template v-slot:activator="{ on, attrs }">
                <v-card
                  class="portrait"
                  img="https://placekitten.com/600/600"
                  height="50"
                  width="50"
                  v-bind="attrs"
                  v-on="on"
                ></v-card>
              </template>
              <v-list>
                <v-list-item
                  v-for="(item, index) in items"
                  :key="index"
                  @click="handleClick(index)"
                >
                  <v-list-item-title>{{ item.title }}</v-list-item-title>
                </v-list-item>
              </v-list>
            </v-menu>
          </div>

          <v-dialog v-model="logoutDialog" max-width="320">
            <layout-the-dialog @disagree="closeDialog" @agree="logout"
              >>
              <template v-slot:text> Do you really want to logout? </template>
            </layout-the-dialog>
          </v-dialog>
        </template>

        <v-dialog v-model="loginDialog" max-width="600px">
          <template v-slot:activator="{ on, attrs }">
            <v-btn v-bind="attrs" v-on="on" color="primary" :small="true"
              >Sign in</v-btn
            >
          </template>
        <auth-dialog v-if="loginDialog"></auth-dialog>
        </v-dialog>
      </div>
    </v-toolbar>
  </v-card>
</template>

<script>
import AuthDialog from "~/components/AuthDialog.vue";

export default {
  components: { AuthDialog },
  data() {
    return {
      loginDialog: false,
      logoutDialog: false,
      items: [
        {
          title: "Profile",
          click() {
            this.$router.push("/profile");
          },
        },
        {
          title: "Settings",
          click() {
            this.$router.push("/settings");
          },
        },
        {
          title: "Logout",
          click() {
            this.dialog = true;
          },
        },
      ],
      breadcrumbs: [
        {
          text: "Test1",
          disabled: false,
          href: "auth/login",
        },
        {
          text: "Test2",
          disabled: false,
          href: "auth/login",
        },
        {
          text: "Test2",
          disabled: false,
          href: "auth/login",
        },
      ],
    };
  },
  computed: {
    loggedIn() {
      // return this.$store.getters['auth/loggedIn'];
      return false;
    },
    title() {
      switch (this.$vuetify.breakpoint.name) {
        case "xs":
          return "C";
        default:
          return "CHATTY";
      }
    },
  },
  methods: {
    logout() {
      this.dialog = false;
      // this.$store.dispatch('auth/logout');
      this.$router.replace("/");
    },
    closeDialog() {
      this.dialog = false;
    },
    handleClick(index) {
      this.items[index].click.call(this);
    },
  },
};
</script>

<style lang="scss" scoped>
.links {
  text-decoration: none;
  color: $primaryColor;
}
.icon {
  color: $primaryColor;
}

h1 {
  display: flex;
  justify-content: center;
  color: $primaryColor;
}

@media (max-width: 767px) {
  .logAlert {
    margin-top: 10px !important;
  }
}
</style>
