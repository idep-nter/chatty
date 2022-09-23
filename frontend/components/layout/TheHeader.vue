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
      <v-breadcrumbs :items="breadcrumbsLeft">
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
          <v-dialog v-model="dialog" max-width="320">
            <layout-the-dialog @disagree="closeDialog" @agree="logout"
              >>
              <template v-slot:text> Do you really want to logout? </template>
            </layout-the-dialog>
          </v-dialog>
        </template>

        <!-- <NuxtLink to="/auth/login" class="links" v-else>
          <v-btn color="primary" :small="buttonSize">Sign in</v-btn>
        </NuxtLink> -->
          <v-breadcrumbs :items="breadcrumbsRight">
            <template v-slot:item="{ item }">
              <v-breadcrumbs-item :href="item.href" :disabled="item.disabled">
                {{ item.text.toUpperCase() }}
              </v-breadcrumbs-item>
            </template>
          </v-breadcrumbs>
      </div>
    </v-toolbar>
  </v-card>
</template>

<style lang="scss" scoped>
.links {
  text-decoration: none;
  color: $primaryColor;
}
.icon {
  color: $primaryColor;
}
</style>

<script>
export default {
  data() {
    return {
      dialog: false,
      // items: [
      //   {
      //     title: "Profile",
      //     click() {
      //       this.$router.push("/profile");
      //     },
      //   },
      //   {
      //     title: "Settings",
      //     click() {
      //       this.$router.push("/settings");
      //     },
      //   },
      //   {
      //     title: "Logout",
      //     click() {
      //       this.dialog = true;
      //     },
      //   },
      // ],
      breadcrumbsLeft: [
        {
          text: 'Test1',
          disabled: false,
          href: 'auth/login',
        },
        {
          text: 'Test2',
          disabled: false,
          href: 'auth/login',
        },
        {
          text: 'Test2',
          disabled: false,
          href: 'auth/login',
        },
      ],
      breadcrumbsRight: [
        {
          text: 'login',
          disabled: false,
          href: 'auth/login',
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
    buttonSize() {
      switch (this.$vuetify.breakpoint.name) {
        case "xs":
          return true;
        default:
          return false;
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
    goTo(payload) {},
  },
};
</script>
