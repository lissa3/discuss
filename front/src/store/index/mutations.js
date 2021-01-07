export const mutations = {
    //for search via menu search bar
    SET_LOOK_UP(state,term){state.lookUp = term},  
    SET_DISPLAY_NAME(state,newName){state.displayName = newName;},
    // user
    // SET_USER_ID(state,userId){state.currentUserId = userId;},
    SET_PROFILE(state,newProfile){state.tempProfile = newProfile;},         
    DESTROY_PROFILE(state){
      localStorage.removeItem('profile');
      state.profile = "";
    },
    // AUTH_REQUEST(state){state.auth_request="loading"},
    UPDATE_API_IDEAS(state,ideas){    
      state.APIDataIdeas= ideas;    
    }
}