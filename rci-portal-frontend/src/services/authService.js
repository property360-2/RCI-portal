import apiClient from './api'

/**
 * Authentication Service
 * Handles all auth-related API calls
 */
const authService = {
  /**
   * Register new user
   * @param {Object} userData - User registration data
   * @returns {Promise} Response with user data
   */
  register: async (userData) => {
    const response = await apiClient.post('/auth/register/', {
      username: userData.username,
      email: userData.email,
      password: userData.password,
      first_name: userData.firstName,
      last_name: userData.lastName,
      role: userData.role || 'student',
    })
    return response.data
  },

  /**
   * Login user
   * @param {string} username
   * @param {string} password
   * @returns {Promise} Response with token and user data
   */
  login: async (username, password) => {
    const response = await apiClient.post('/auth/login/', {
      username,
      password,
    })
    return response.data
  },

  /**
   * Logout user
   * @returns {Promise}
   */
  logout: async () => {
    try {
      await apiClient.post('/auth/logout/')
    } catch (error) {
      console.error('Logout error:', error)
    }
  },

  /**
   * Refresh access token
   * @param {string} refreshToken
   * @returns {Promise}
   */
  refreshToken: async (refreshToken) => {
    const response = await apiClient.post('/auth/refresh/', {
      refresh: refreshToken,
    })
    return response.data
  },

  /**
   * Get current user profile
   * @returns {Promise}
   */
  getCurrentUser: async () => {
    const response = await apiClient.get('/users/me/')
    return response.data
  },

  /**
   * Update user profile
   * @param {Object} userData - Updated user data
   * @returns {Promise}
   */
  updateProfile: async (userData) => {
    const response = await apiClient.patch('/users/me/', userData)
    return response.data
  },

  /**
   * Change password
   * @param {string} oldPassword
   * @param {string} newPassword
   * @returns {Promise}
   */
  changePassword: async (oldPassword, newPassword) => {
    const response = await apiClient.post('/auth/change-password/', {
      old_password: oldPassword,
      new_password: newPassword,
    })
    return response.data
  },

  /**
   * Request password reset
   * @param {string} email
   * @returns {Promise}
   */
  requestPasswordReset: async (email) => {
    const response = await apiClient.post('/auth/password-reset/', {
      email,
    })
    return response.data
  },
}

export default authService