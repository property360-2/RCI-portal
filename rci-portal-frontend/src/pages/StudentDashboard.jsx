import { 
  GraduationCap, 
  BookOpen, 
  FileText, 
  Bell, 
  TrendingUp,
  Calendar,
  Clock,
  Award,
  ArrowRight
} from 'lucide-react'
import useAuthStore from '../store/useAuthStore'
import DashboardLayout from '../components/layout/DashboardLayout'

const StudentDashboard = () => {
  const user = useAuthStore((state) => state.user)

  const stats = [
    { 
      label: 'Enrolled Subjects', 
      value: '7', 
      icon: BookOpen, 
      color: 'blue',
      change: '+2 from last semester',
      bgGradient: 'from-blue-500 to-blue-600'
    },
    { 
      label: 'Current GPA', 
      value: '3.45', 
      icon: TrendingUp, 
      color: 'green',
      change: '+0.12 this semester',
      bgGradient: 'from-green-500 to-emerald-600'
    },
    { 
      label: 'Completed Units', 
      value: '84', 
      icon: Award, 
      color: 'purple',
      change: '36 units remaining',
      bgGradient: 'from-purple-500 to-purple-600'
    },
    { 
      label: 'Pending Tasks', 
      value: '3', 
      icon: Bell, 
      color: 'orange',
      change: '2 due this week',
      bgGradient: 'from-orange-500 to-orange-600'
    },
  ]

  const recentSubjects = [
    { code: 'CS 101', name: 'Introduction to Programming', professor: 'Dr. Smith', schedule: 'MWF 10:00-11:30 AM', progress: 75 },
    { code: 'MATH 201', name: 'Calculus II', professor: 'Dr. Johnson', schedule: 'TTH 1:00-2:30 PM', progress: 60 },
    { code: 'ENG 102', name: 'Technical Writing', professor: 'Prof. Williams', schedule: 'MWF 2:00-3:30 PM', progress: 85 },
  ]

  const upcomingEvents = [
    { title: 'Midterm Exam - CS 101', date: 'Oct 15, 2025', time: '10:00 AM', type: 'exam' },
    { title: 'Project Submission - MATH 201', date: 'Oct 18, 2025', time: '11:59 PM', type: 'assignment' },
    { title: 'Quiz - ENG 102', date: 'Oct 20, 2025', time: '2:00 PM', type: 'quiz' },
  ]

  const announcements = [
    { title: 'Enrollment for Next Semester Opens', date: 'Oct 12, 2025', category: 'Registration' },
    { title: 'Library Hours Extended During Finals', date: 'Oct 10, 2025', category: 'Facilities' },
    { title: 'Career Fair Next Month', date: 'Oct 8, 2025', category: 'Events' },
  ]

  return (
    <DashboardLayout>
      <div className="min-h-screen bg-gradient-to-br from-gray-50 to-gray-100">
        <div className="p-6 max-w-7xl mx-auto">
          {/* Welcome Header */}
          <div className="mb-8">
            <h1 className="text-4xl font-bold text-gray-900 mb-2">
              Welcome back, <span className="text-blue-600">{user?.username || 'Student'}</span>! 👋
            </h1>
            <p className="text-gray-600 text-lg">Here's what's happening with your academics today</p>
          </div>

          {/* Stats Cards */}
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
            {stats.map((stat, index) => (
              <div
                key={index}
                className="bg-white rounded-2xl shadow-lg hover:shadow-xl transition-all duration-300 overflow-hidden group hover:-translate-y-1"
              >
                <div className={`h-2 bg-gradient-to-r ${stat.bgGradient}`}></div>
                <div className="p-6">
                  <div className="flex items-center justify-between mb-4">
                    <div className={`p-3 bg-gradient-to-r ${stat.bgGradient} rounded-xl`}>
                      <stat.icon className="w-6 h-6 text-white" />
                    </div>
                    <span className="text-3xl font-bold text-gray-900">{stat.value}</span>
                  </div>
                  <h3 className="text-sm font-medium text-gray-600 mb-1">{stat.label}</h3>
                  <p className="text-xs text-gray-500">{stat.change}</p>
                </div>
              </div>
            ))}
          </div>

          <div className="grid grid-cols-1 lg:grid-cols-3 gap-6 mb-8">
            {/* Current Subjects */}
            <div className="lg:col-span-2 bg-white rounded-2xl shadow-lg p-6">
              <div className="flex items-center justify-between mb-6">
                <h2 className="text-2xl font-bold text-gray-900 flex items-center gap-2">
                  <BookOpen className="w-6 h-6 text-blue-600" />
                  Current Subjects
                </h2>
                <button className="text-blue-600 hover:text-blue-700 font-medium text-sm flex items-center gap-1">
                  View All
                  <ArrowRight className="w-4 h-4" />
                </button>
              </div>
              <div className="space-y-4">
                {recentSubjects.map((subject, index) => (
                  <div
                    key={index}
                    className="p-4 border border-gray-200 rounded-xl hover:border-blue-300 hover:shadow-md transition-all duration-200 group"
                  >
                    <div className="flex items-start justify-between mb-3">
                      <div>
                        <div className="flex items-center gap-2 mb-1">
                          <span className="px-2 py-1 bg-blue-100 text-blue-700 text-xs font-semibold rounded">
                            {subject.code}
                          </span>
                          <span className="text-xs text-gray-500">{subject.schedule}</span>
                        </div>
                        <h3 className="font-semibold text-gray-900 group-hover:text-blue-600 transition-colors">
                          {subject.name}
                        </h3>
                        <p className="text-sm text-gray-600 mt-1">{subject.professor}</p>
                      </div>
                      <button className="px-4 py-2 text-sm font-medium text-blue-600 hover:bg-blue-50 rounded-lg transition-colors">
                        View
                      </button>
                    </div>
                    <div className="space-y-1">
                      <div className="flex items-center justify-between text-xs text-gray-600">
                        <span>Progress</span>
                        <span className="font-medium">{subject.progress}%</span>
                      </div>
                      <div className="w-full bg-gray-200 rounded-full h-2">
                        <div
                          className={`h-2 rounded-full bg-gradient-to-r ${
                            subject.progress >= 80 ? 'from-green-500 to-emerald-600' :
                            subject.progress >= 60 ? 'from-blue-500 to-blue-600' :
                            'from-orange-500 to-orange-600'
                          }`}
                          style={{ width: `${subject.progress}%` }}
                        ></div>
                      </div>
                    </div>
                  </div>
                ))}
              </div>
            </div>

            {/* Upcoming Events */}
            <div className="bg-white rounded-2xl shadow-lg p-6">
              <div className="flex items-center gap-2 mb-6">
                <Calendar className="w-6 h-6 text-purple-600" />
                <h2 className="text-2xl font-bold text-gray-900">Upcoming</h2>
              </div>
              <div className="space-y-3">
                {upcomingEvents.map((event, index) => (
                  <div
                    key={index}
                    className="p-4 border-l-4 border-purple-500 bg-purple-50 rounded-r-xl hover:bg-purple-100 transition-colors"
                  >
                    <div className="flex items-start gap-3">
                      <div className={`p-2 rounded-lg ${
                        event.type === 'exam' ? 'bg-red-100' :
                        event.type === 'assignment' ? 'bg-blue-100' :
                        'bg-green-100'
                      }`}>
                        <Clock className={`w-4 h-4 ${
                          event.type === 'exam' ? 'text-red-600' :
                          event.type === 'assignment' ? 'text-blue-600' :
                          'text-green-600'
                        }`} />
                      </div>
                      <div className="flex-1">
                        <h3 className="font-semibold text-gray-900 text-sm mb-1">
                          {event.title}
                        </h3>
                        <p className="text-xs text-gray-600">{event.date}</p>
                        <p className="text-xs text-gray-500">{event.time}</p>
                      </div>
                    </div>
                  </div>
                ))}
              </div>
              <button className="w-full mt-4 py-2 text-sm font-medium text-purple-600 hover:bg-purple-50 rounded-lg transition-colors">
                View Calendar
              </button>
            </div>
          </div>

          {/* Announcements & Quick Actions */}
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
            {/* Announcements */}
            <div className="bg-white rounded-2xl shadow-lg p-6">
              <div className="flex items-center gap-2 mb-6">
                <Bell className="w-6 h-6 text-orange-600" />
                <h2 className="text-2xl font-bold text-gray-900">Announcements</h2>
              </div>
              <div className="space-y-3">
                {announcements.map((announcement, index) => (
                  <div
                    key={index}
                    className="p-4 border border-gray-200 rounded-xl hover:border-orange-300 hover:shadow-sm transition-all"
                  >
                    <div className="flex items-start justify-between">
                      <div className="flex-1">
                        <div className="flex items-center gap-2 mb-1">
                          <span className="px-2 py-1 bg-orange-100 text-orange-700 text-xs font-semibold rounded">
                            {announcement.category}
                          </span>
                          <span className="text-xs text-gray-500">{announcement.date}</span>
                        </div>
                        <h3 className="font-semibold text-gray-900">{announcement.title}</h3>
                      </div>
                    </div>
                  </div>
                ))}
              </div>
              <button className="w-full mt-4 py-2 text-sm font-medium text-orange-600 hover:bg-orange-50 rounded-lg transition-colors">
                View All Announcements
              </button>
            </div>

            {/* Quick Actions */}
            <div className="bg-gradient-to-br from-blue-600 to-indigo-700 rounded-2xl shadow-lg p-6 text-white">
              <h2 className="text-2xl font-bold mb-6">Quick Actions</h2>
              <div className="space-y-3">
                <button className="w-full bg-white/20 hover:bg-white/30 backdrop-blur-sm p-4 rounded-xl text-left transition-all hover:scale-105 transform">
                  <div className="flex items-center gap-3">
                    <div className="p-2 bg-white/20 rounded-lg">
                      <FileText className="w-5 h-5" />
                    </div>
                    <div>
                      <h3 className="font-semibold">Request Documents</h3>
                      <p className="text-sm text-blue-100">Get official transcripts</p>
                    </div>
                  </div>
                </button>
                
                <button className="w-full bg-white/20 hover:bg-white/30 backdrop-blur-sm p-4 rounded-xl text-left transition-all hover:scale-105 transform">
                  <div className="flex items-center gap-3">
                    <div className="p-2 bg-white/20 rounded-lg">
                      <GraduationCap className="w-5 h-5" />
                    </div>
                    <div>
                      <h3 className="font-semibold">Enroll Subjects</h3>
                      <p className="text-sm text-blue-100">Register for next semester</p>
                    </div>
                  </div>
                </button>
                
                <button className="w-full bg-white/20 hover:bg-white/30 backdrop-blur-sm p-4 rounded-xl text-left transition-all hover:scale-105 transform">
                  <div className="flex items-center gap-3">
                    <div className="p-2 bg-white/20 rounded-lg">
                      <Award className="w-5 h-5" />
                    </div>
                    <div>
                      <h3 className="font-semibold">View Grades</h3>
                      <p className="text-sm text-blue-100">Check your performance</p>
                    </div>
                  </div>
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </DashboardLayout>
  )
}

export default StudentDashboard