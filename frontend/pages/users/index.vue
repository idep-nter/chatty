<template>
  <v-row class="mt-12 mainRow d-flex justify-center">
    <v-col md="8" sm="7" class>
      <v-card width="1400" height="100" class="pa-2 filterCard">
        <v-row>
          <v-col cols="4">
            <v-text-field
              dense
              class="ml-5 mt-6"
              prepend-icon="mdi-magnify"
              flat
              outlined
              placeholder="Search by name"
              filled
              v-model="searchedName"
            ></v-text-field>
          </v-col>
          <v-col cols="3">
            <v-container id="dropdown-example-1">
              <v-overflow-btn
                filled
                v-model="sortBy"
                dense
                class="sortBy"
                :items="sorts"
                label="Sort by"
              ></v-overflow-btn>
            </v-container>
          </v-col>
          <v-col cols="2">
            <v-container class="px-0" fluid>
              <v-checkbox
                v-model="onlineUsers"
                label="Online"
              ></v-checkbox>
            </v-container>
          </v-col>
          
        </v-row>
      </v-card>
    </v-col>
    <v-col md="8" sm="7">
      <v-card width="1400" height="695" class="pa-2 itemCard">
        <!-- <user-list-item
          v-for="(thread, index) in filteredUsers"
          :key="thread.id"
          :id="thread.id"
          :number="index + 1"
          :title="thread.name"
        >
        </user-list-item> -->

        <v-pagination id="pagination" color="primary"></v-pagination>
      </v-card>
    </v-col>
  </v-row>
</template>

<script>
import UserListItem from '~/components/users/UserListItem.vue';


export default {
  components: { UserListItem },
  data() {
    return {
      users: []
    };
  },
  created() {
    // this.$store.dispatch('users/loadUsers');
    this.users = this.$store.getters['users/getUsers']
  },
  computed: {
    onlineUsers() {

    },
    filteredUsers() {
      // filter by name
      let filtered = this.users.filter((user) => {
        return user.username
          .toLowerCase()
          .includes(this.searchedName.toLowerCase());
      });
      // sort + number of posts + registered
      if (this.sortBy == 'Alphabetically') {
        filtered.sort((a, b) => {
          let ta = a.username.toLowerCase(),
            tb = b.username.toLowerCase();

          if (ta < tb) {
            return -1;
          }
          if (ta > tb) {
            return 1;
          }
          return 0;
        });
      // } else if (this.sortBy == 'Date of registration') {
      //   filtered.sort((a, b) => {
      //     let da = new Date(a.registered),
      //       db = new Date(b.registered);
      //     return da - db;
      //   });
      }

      return filtered;
    },
  },
  methods: {
  },
};
</script>

<style scoped>
.sortBy {
  margin-top: 10px;
}
li {
  list-style-type: none;
}
#pagination {
  position: absolute;
  bottom: 13%;
  left: 0%;
  right: 0%;
}

#create {
  position: absolute;
  bottom: 3%;
  left: 0%;
  right: 0%;
}

/* a {
    text-decoration: none;
    color: #006400;
  } */

/* Smartphones */
/* @media (max-width: 767px) {
    .itemCard {
      height: 1300px !important;
    }
    .mainRow {
      margin-top: 0px !important;
    }
  }
   */
/* Tablets */
/* @media (min-width: 768px) and (max-width: 991px) {
    .mainRow {
      justify-content: center;
    }
  }
  
  /* Desktop */
/* @media (min-width: 992px) {
    .filterCard {
      margin-left: 25px;
    }
  } */
</style>
