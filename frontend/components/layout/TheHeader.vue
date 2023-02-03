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
      <v-breadcrumbs :items="breadcrumbs" class="bread">
        <template v-slot:item="{ item }">
          <v-breadcrumbs-item @click="handleClick(breadcrumbs, item.index)">
            {{ item.text.toUpperCase() }}
          </v-breadcrumbs-item>
        </template>
      </v-breadcrumbs>

      <Transition name="fade">
        <v-text-field
          v-if="searchbar"
          style="width: 700px"
          dense
          class="ml-10 mt-7"
          prepend-icon="mdi-magnify"
          flat
          rounded
          placeholder="Search"
          filled
          v-model="search"
        ></v-text-field>
      </Transition>

      <v-spacer></v-spacer>

      <div class="right">
        <template v-if="loggedIn">
          <div class="text-center">
            <v-menu offset-y transition="scroll-y-transition">
              <template v-slot:activator="{ on, attrs }">
                <v-card
                  class="portrait mr-4"
                  :img="image"
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
                  @click="handleClick(items, index)"
                >
                  <v-list-item-title>{{ item.title }}</v-list-item-title>
                </v-list-item>
              </v-list>
            </v-menu>
          </div>

          <v-dialog persistent v-model="logoutDialog" max-width="320">
            <layout-the-dialog @disagree="logoutDialog = false" @agree="logout"
              >>
              <template v-slot:text> Do you really want to logout? </template>
            </layout-the-dialog>
          </v-dialog>
        </template>

        <template v-else>
          <v-dialog persistent v-model="loginDialog" max-width="600px">
            <template v-slot:activator="{ on, attrs }">
              <v-btn v-bind="attrs" v-on="on" color="primary" :small="true"
                >Sign in</v-btn
              >
            </template>
            <register-dialog
              v-if="!loginMode"
              @toggle-auth="toggleAuth"
              @close-dialog="loginDialog = false"
            ></register-dialog>
            <login-dialog
              v-else
              @toggle-auth="toggleAuth"
              @close-dialog="loginDialog = false"
            ></login-dialog>
          </v-dialog>
        </template>
      </div>
    </v-toolbar>
  </v-card>
</template>

<script>
import RegisterDialog from '~/components/dialogs/RegisterDialog.vue';
import LoginDialog from '~/components/dialogs/LoginDialog.vue';

export default {
  components: { RegisterDialog, LoginDialog },
  data() {
    return {
      search: '',
      searchbar: true,
      loginDialog: false,
      logoutDialog: false,
      loginMode: true,
      userId: '',
      image: '',
      items: [
        {
          title: 'Profile',
          click() {
            this.$router.push({ path: `/users/${this.userId}` });
          },
        },
        {
          title: 'Settings',
          click() {
            this.$router.push('/settings');
          },
        },
        {
          title: 'Logout',
          click() {
            this.logoutDialog = true;
          },
        },
      ],
      breadcrumbs: [
        {
          index: 0,
          text: 'threads',
          click() {
            this.$router.push('/threads');
          },
        },
        {
          index: 1,
          text: 'TBD',
          click() {},
        },
        {
          index: 2,
          text: 'search',
          click() {
            this.searchbar = !this.searchbar;
          },
        },
      ],
    };
  },
  computed: {
    loggedIn() {
      return this.$store.getters['auth/loggedIn'];
    },
    title() {
      switch (this.$vuetify.breakpoint.name) {
        case 'xs':
          return 'C';
        default:
          return 'CHATTY';
      }
    },
  },
  watch: {
    loggedIn(val) {
      this.loadStuff()
    }
  },
  methods: {
    logout() {
      this.$store.dispatch('auth/logout');
      this.loginDialog = false;
      this.logoutDialog = false;
      this.$router.replace('/');
    },
    handleClick(items, index) {
      items[index].click.call(this);
    },
    toggleAuth() {
      this.loginMode = !this.loginMode;
    },
    async loadStuff() {
      await this.$store.dispatch('users/loadUsers');
      await this.$store.dispatch('users/loadUserId');
      this.userId = this.$store.getters['users/getUserId']
      this.image = this.$store.getters['users/getUserInfo'](this.userId).image;
    }
  },
  created() {
    this.loadStuff()
  },
};
</script>

<style lang="scss" scoped>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s ease;
}

.fade-enter,
.fade-leave-to {
  opacity: 0;
}
.bread {
  color: $primaryColor;
  cursor: pointer;
}
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
