import apiClient from './api'

const studentService = {
    /**
     * Get current student profile
     */
    getMyProfile: async () => {
        const response = await apiClient.get('/students/', {
            params: { user: 'me' } // Backend filters by current user
        })
        return response.data.results?.[0] || response.data[0]
    },

    /**
     * Get enrolled subjects/sections for current term
     */
    getMyEnrollments: async (term = null) => {
        const params = {}
        if (term) params.term = term

        const response = await apiClient.get('/enrollments/', { params })
        return response.data
    },

    /**
     * Get my grades
     */
    getMyGrades: async () => {
        const response = await apiClient.get('/grades/')
        return response.data
    },

    /**
     * Get subjects for a specific curriculum
     */
    getSubjects: async (curriculumId = null) => {
        const params = {}
        if (curriculumId) params.curriculum = curriculumId

        const response = await apiClient.get('/subjects/', { params })
        return response.data
    },

    /**
     * Enroll in a section
     */
    enrollInSection: async (sectionId, term) => {
        const response = await apiClient.post('/enrollments/', {
            section: sectionId,
            term,
            status: 'pending'
        })
        return response.data
    },
}

export default studentService